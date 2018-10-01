def find_max(list_check):
    max_num = 0
    for num in list_check:
        max_num = max(max_num,num)
    return max_num

def count_entries(list_check, num_check):
    count = 0
    for num in list_check:
        if num == num_check:
            count += 1
    return count

def hash_list(list_check):
    number = 0
    counts = [0] * 1000
    for x in range(0, len(list_check)):
        counts[list_check[x]] += 1
    return_str = ""
    for x in range(0, len(counts)):
        return_str += str(x) + "x" + str(counts[x])
    return return_str

hashed_mins = {}
current_splits = {}
def permute(time_left, patrons, orig_time):
    global hashed_mins
    global weird_case
    global current_splits
    if time_left <= 0:
        return orig_time
    if hash_list(patrons) in hashed_mins:
        return hashed_mins[hash_list(patrons)]
    mini = orig_time
    entries = count_entries(patrons, find_max(patrons))
    if entries > time_left:
        return orig_time
    for x in range(0, len(patrons)):
        if patrons[x] < 4:
            continue
        if not patrons[x] in current_splits:
            start_time = patrons[x] - 2
            for t in range(start_time,patrons[x]/2 - 1,-1):
                current_splits[patrons[x]] = [t, patrons[x] - t]
                new_list = patrons + [t]
                new_list[x] = patrons[x] - t
                mini = min(mini, min(find_max(new_list) + orig_time - time_left,permute(time_left - 1, new_list, orig_time)))
                hashed_mins[hash_list(new_list)] = mini
                del current_splits[patrons[x]]
        else:
            changes = current_splits[patrons[x]]
            new_list = patrons + [changes[0]]
            new_list[x] = changes[1]
            mini = min(mini, min(find_max(new_list) + orig_time - time_left,permute(time_left - 1, new_list, orig_time)))
            hashed_mins[hash_list(new_list)] = mini
            
    return mini
    
def brute_force(n_patrons, patrons):
    patrons_num = []
    min_time = 0
    for patron in patrons:
        int_patron = int(patron)
        min_time = max(min_time, int_patron)
        patrons_num.extend([int_patron])

    return permute(min_time - 1, patrons_num, min_time)

    
file_name = "B-small-attempt1"
#file_name = "B-small-attempt0"
file_handle = open(file_name + ".in")
output_file = open(file_name + ".out", 'w')

weird_case = False

test_cases = int(file_handle.readline())

for x in range(0,test_cases):
    hashed_mins = {}
    n_patrons = int(file_handle.readline())
    patrons = file_handle.readline().strip().split(" ")

    output_file.write("Case #{0}: {1}\n".format(str(x+1), str(brute_force(n_patrons, patrons))))
    print x
    

file_handle.close()
output_file.close()




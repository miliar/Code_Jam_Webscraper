def solution(case):
    input_in = input()
    tmp_in = input_in.split(" ")

    stall_num = int(tmp_in[0])
    people_num = int(tmp_in[1])

    stalls = "0"*stall_num+"1"
    stall_num += 1

    insert_stall = 0
    for person in range(0, people_num):
        has_idx = [i for i, x in enumerate(stalls) if x == "1"]
        dist = []
        for idx, val in enumerate(has_idx):
            if idx == 0:
                dist.append(int(has_idx[idx]))
            else:
                dist.append(int(has_idx[idx])-int(has_idx[idx-1])-1)

        max_value = max(dist)
        max_index = dist.index(max_value)
        insert_stall = has_idx[max_index]
        insert_stall -= int(max_value/2)+1

        tmp_stalls = list(stalls)
        tmp_stalls[insert_stall] = "1"
        stalls = ''.join(tmp_stalls)

    left = stalls[:insert_stall]
    right = stalls[insert_stall+1:]
    
    left = left[::-1]
    left_min = 0
    try:
        left_min = left.index("1")
    except:
        left_min = len(left)

    right_min = 0
    try:
        right_min = right.index("1")
    except:
        right_min = len(right)

    print("Case #" + str(case) + ": " + str(right_min) + " " + str(left_min))

if __name__ == "__main__":
    cases = input()
    for case in range(1, int(cases)+1):
        solution(case)

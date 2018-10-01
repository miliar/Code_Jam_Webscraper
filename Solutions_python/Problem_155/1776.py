import time

start = time.time()

def standingOvation(n, people):
    ppl_needed = 0

    #People under max shyness
    total_ppl = 0

    if (int(people) == 0):
        return 0
    for i,j in enumerate(people):
        if int(j) > 0 and total_ppl < i:
            ppl_needed += i - total_ppl
            total_ppl += i - total_ppl
        total_ppl += int(j)
    
    #for i in range(len(people)-1):
    #    total_ppl += int(people[i])

    #ppl_needed = n - total_ppl

    if (ppl_needed > 0):
        return ppl_needed
    else:
        return 0

def is_int(n):
    try:
        int(n)
        return True
    except:
        return False

in_filename = "A-large.in"
out_filename = "output.txt"

with open(in_filename, 'r') as f_in:
    with open(out_filename, 'w') as f_out:
        for count, line in enumerate(f_in.readlines()):
            line = line.strip()
            words = line.split(" ")
            #print(words)
            if len(words) == 2 and is_int(words[1]):
                #print(words)
                f_out.write("Case #{}: {}\n".format(count, standingOvation(int(words[0]), words[1])))
                print("Case #{}: {}\n".format(count, standingOvation(int(words[0]), words[1])))
            
        
print(time.time()-start)

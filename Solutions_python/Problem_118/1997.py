from shlex import split

def read_file():
    f = open("qc_in.txt")
    global a
    a = f.readlines()
    global test_cases
    assert int(a[0])
    test_cases = int(a.pop(0))
    a = [s.strip("\n") for s in a]
    f.close()
    
def convert_data():
    global starts
    starts = []
    global ends
    ends = []
    for i in range(test_cases):
        nums = split(a[i])
        starts.append(int(nums[0]))
        ends.append(int(nums[1])+1)

def is_palindrome(num):
    nstr = str(num)
    pal = nstr[::-1]
    return int(pal) == num

def find_fasnos():
    global results
    results = []
    for i in range(test_cases):
        found = 0
        for n in range(starts[i], ends[i]):
            # optimization: range is sqrts of ns
            if n == round(n**0.5, 8)**2:
                if is_palindrome(n) and is_palindrome(int(round(n**0.5, 8))):
                    found += 1
        results.append(found)
    
def write_to_file():
    f2 = open("qc_out.txt", 'wt') 
    for i in range(len(results)):
        f2.writelines("Case #"+str(i+1)+": "+str(results[i])+"\n")   
    f2.close()

def debug():
    print starts
    print ends
    print results

def main():   
    read_file()
    convert_data()
    find_fasnos()
    write_to_file()
    debug()

if __name__ == "__main__":
    main()

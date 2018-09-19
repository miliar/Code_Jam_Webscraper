import math

def main():
    inf = open("small.in")
    outf = open("small.out", "w")
    
    fs = load_fs()
    
    nr = int(inf.readline())
    for i, line in enumerate(inf):
        tokens = line.split(" ")
        a = int(tokens[0])
        b = int(tokens[1])
        result = solve_with_fs(a, b, fs)
        outf.write("Case #%s: %s\n" % (str(i+1), str(result)))
        print ("Case #%s: %s\n" % (str(i+1), str(result)))
    inf.close()
    outf.close()
        
def solve(a, b):
    fsf = open("fs_large.txt", "w")
    start = int(math.floor(math.sqrt(a)) - 1)
    fairsquare = 0
    for i in range(start, b + 1):
        if isPalindrome(i):
            square = i**2
            if square < a:
                continue;
            if square <= b:
                if isPalindrome(square):
                    print(str(square) + "\t" + str(i))
                    fsf.write(str(square) + "\t" + str(i) + "\n")
                    fsf.flush()
                    fairsquare += 1
                else:
                    pass
            else:
                fsf.close()
                return fairsquare
        else:
            pass
    fsf.close()
    return fairsquare
                 

def isPalindrome(num):
    s = str(num)
    return s == s[::-1]


def load_fs():
    fsf = open("xlarge_fs_post.txt")
    fs = []
    for line in fsf:
        fs.append(int(line.strip()))
    return fs

def solve_with_fs(a, b, fs):
    count = 0
    for n in fs:
        if n > b:
            return count
        if n >= a and n <= b:
            count += 1
    return count

if __name__ == '__main__':
    main()    
    #solve(1, 10**100)
    
    
def palindrome(L):
    return L == L[::-1]

def reader(inFile):
    (start, end) = inFile.getInts()
    return (start, end)

def solver((start, end)):
    print start, end
    i = 1
    count = 0
    while True:
        j = i * i
        if j < start or not palindrome(str(i)):
            i += 1
            continue
        i += 1
        if j > end:
            break
        if palindrome(str(j)):
            print j
            count+=1
    return count

if __name__ == "__main__":
    from GCJ import GCJ
    GCJ(reader, solver, "/Users/robot9/Projects/gcj/", "C").run()

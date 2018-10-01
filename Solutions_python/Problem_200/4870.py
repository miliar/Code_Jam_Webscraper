def check(number):
    val = str(number)
    for i in range(len(val)-1):
        if int(val[i+1]) - int(val[i]) < 0:
            return False
    return True

def find(n):
    if n < 10:
        return n
    result = check(n)
    try:
        ob = int(str(n), 2) # just to check it contains 0 and 1
        val = str(n)
        result = ""
        for i in range(len(val)-1):
            result = result + "9"
        return int(result)
    except:
        pass
    while not result:
        n = n - 1
        result = check(n)
    return n

def main():
    tests = int(input())
    for i in range(tests):
        N = int(input())
        print "Case #"+str(i+1)+": "+str(find(N))

main()

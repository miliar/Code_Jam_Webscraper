

def main():
    cases = int(input())
    for i in range(cases):
        num = int(input())
        highest = check(num)
        out = "Case #" + repr(i+1) + ": " + repr(highest)
        print(out)



def check(num):
    for i in range(int(num), 0, -1):
        if check_tidy(i):
            break
    return i

def check_tidy(num):
    num = str(num)
    for i in range(0, len(num)-1):
        if num[i] > num[i+1] :
            return False 
            
    return True




if __name__ == '__main__':
    main()

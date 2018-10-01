def x(num):
    nd = num % 10
    num = num // 10
    while(num):
        d = num % 10
        if d > nd:
            return False
        nd = d
        num = num // 10
    return True

def tidy(num):
    while(not x(num)):
        num = num - 1
    return num
        
        

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        print("Case #" + str(_+1) + ": " +
              str(tidy(int(input())))
              )
        
    

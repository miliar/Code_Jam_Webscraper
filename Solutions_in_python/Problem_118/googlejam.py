def is_palindrome(n, partial=0): 
    if n == 0:
        return partial
    return is_palindrome(n / 10, partial * 10 + n % 10)

def is_fair_and_square(apositiveint):
    if apositiveint ==1 or apositiveint==0:
        return True
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    if (is_palindrome(x)==x and is_palindrome(apositiveint)==apositiveint):
        return True
    return False

def test_in_range(low, high, case):
    count = 0
    while(low <= high):
        if(is_fair_and_square(low)):
            count += 1
        low += 1
    with open('res.text', 'a') as res:
        res.write('Case #'+str(case)+': '+str(count)+'\n')

if __name__=="__main__":
    #test_in_range(1, 4, 1)
    with open('test.txt', 'r') as f:
        test = int(f.readline().rstrip('\n'))
        for i in range(1, test + 1):
            bound = f.readline().rstrip('\n').split(' ')
            test_in_range(int(bound[0]), int(bound[1]), i)
    

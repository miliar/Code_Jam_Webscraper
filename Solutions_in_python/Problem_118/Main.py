'''
Template

@author: Mohammad
'''
nums = list(map(str, range(10)))
nums = [''] + nums

def palindrome(s):
    p = []
    for n in nums:
        p.append(s + n + s)
    return p
def isPalindrome(s):
    if len(s) < 2:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:len(s)-1])
psq = [1, 4, 9]
for i in range(1,1000000):    
    for j in palindrome(str(i)):
       sq = str(int(j)*int(j))
       if isPalindrome(sq):
           psq.append(int(sq))
psq = sorted(psq)
def main():  
    inn = open("C-small-attempt0.in", "r")
    out = open("out.txt", "w")
    T = int(inn.readline())
    for t in range(T):
        [A,B] = [int(n) for n in inn.readline().split()]
        count = 0
        for pq in psq:
            if pq >= A and pq <= B:
                count += 1 
        out.write('Case #' + str(t+1) + ': ' + str(count) + '\n')
        
    inn.close()
    out.close()
main()

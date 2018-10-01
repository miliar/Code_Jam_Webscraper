class TinyNumber(object):
    
    def check_tiny(self, sub):
            sub = str(sub)
            for idx in range(1, len(sub)):
                if sub[idx-1] > sub[idx]:
                    return False
            return True 

    def findLargestNum(self, num):               
        
        print(num)                
        while num > 0:
            if self.check_tiny(num):
                return num
            else:
                num -= 1
        return 0
    
    def findLargestNumFast(self, num):
        
        def check_tiny2(sub):
            numL = list(str(sub))
            reset = False
            
            for idx in range(1, len(numL)):
                if reset is True:
                    numL[idx] = '9'
                elif numL[idx-1] > numL[idx]:                    
                    numL[idx-1] = str(int(numL[idx-1]) - 1)
                    numL[idx] = '9'
                    # print(numL[idx-1])
                    reset = True
            return int(''.join(numL))
        
        # print('case {:d}'.format(num))
        sub = str(num)
         
        res = check_tiny2(num)
        while self.check_tiny(res) is False:
            res = check_tiny2(res)
        
        # print('res {:d}'.format(res))
        # print(pow(10, digits-1) - 1)        
        return res
        
def main():
    sol = TinyNumber()
    
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = [int(s) for s in input().split(" ")]
        res = sol.findLargestNumFast(n[0])
        print("Case #{}: {}".format(i, res))

if __name__ == '__main__':
    main()
  

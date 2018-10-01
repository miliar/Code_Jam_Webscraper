#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals
import heapq

def main():
    in_file = open("B-small-attempt6.in", mode='r')
    out_file = open("B-small-attempt6.out", mode='w')

    lines = in_file.readlines()      
    T = int(lines[0])
    
    def eat(dishes):
        return max(dishes)
    
    def move(dishes, steps):
        dishMax = max(dishes)
        idMax = dishes.index(dishMax)
        dishMin = min(dishes)
        idMin = dishes.index(dishMin)
        
        leastSteps = eat(dishes)+steps        
        
        if dishMax <= 2:
            #print("E", leastSteps, dishes)
            return leastSteps
        
        maxCount = dishes.count(dishMax)
        if (maxCount >= dishMax):
            return leastSteps
            
        secondDish = min(heapq.nlargest(2, dishes)[-1], dishMax-(dishMax/2))
        if (maxCount >= dishMax-secondDish):
            return leastSteps
        
        newDishes = dishes
        for give in range(1, (int((dishMax-dishMin)/2)+1)):
            newDishes[idMax] = dishMax - give
            newDishes[idMin] = dishMin + give
            
            leastSteps = min(leastSteps, move(newDishes, steps+1))
            
        dishes[idMax] = dishMax
        dishes[idMin] = dishMin
        dishes[idMin:] = [0] * len(dishes[idMin:])
        
        #if(leastSteps<eat(dishes)):
        #    print("M", leastSteps, dishes)
        
        return leastSteps

    for i in range(T):
        dishNum = int(lines[2*i + 1])
        dishes = [int(p) for p in lines[2*i + 2].split()]
        
        allDishes = [0] * (sum(dishes)+1)
        allDishes[0:dishNum] = dishes
        
        #print('=' * 60)
        #print(i+1, dishes)
        #print('-' * 60)
        
        ans = move(allDishes, 0)
        
        #print("ans: ", ans)

        
        out_file.write("Case #" + str(i+1) + ": " + str(ans) + "\n") 
        #print("Case #" + str(i+1) + ": " + str(ans) + "\n")
        
        #if i == 3: break
        
        
    in_file.close()
    out_file.close()


if __name__ == '__main__':
    main()

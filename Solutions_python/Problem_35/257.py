'''
Created on 2009-7-10

@author: roamer
'''
from sys import stdout

def findMaxIndex(arr,used):
    maxval = -1
    index = -1
    length = len(arr)
    for i in range(length):
        if(not used[i] and arr[i] > maxval):
            maxval = arr[i]
            index = i
    return  index

if __name__ == "__main__":
    
    f = open('../datain/watersheds.txt','r')
    totalcase =  int(f.readline().strip())
    i = 0
    while i < totalcase:
        map_data = []
        ret_set = []
        H,W = map(int,f.readline().strip().split(' '))
        j = 0
        while j < H:
            map_data.extend(map(int,f.readline().strip().split(' ')))            
            j += 1    
        used = [0] * len(map_data)
        while not all(used):
            part = [findMaxIndex(map_data,used)]
            used[part[0]] = 1
            can_add = True
            while can_add:
                can_add = False
                points = []
                row = part[len(part) - 1] / W
                col = part[len(part) - 1] % W
                if row - 1 >= 0:
                    up = (row - 1) * W + col
                    points.append(up)
                if col - 1 >= 0:
                    left = row * W + col - 1
                    points.append(left)
                if col + 1 < W:
                    right = row * W + col + 1
                    points.append(right)
                if row + 1 < H:
                    down = (row + 1) * W + col
                    points.append(down)
                min_index = -1
                for point in points:
                    if map_data[part[len(part) - 1]] > map_data[point]:
                        if(min_index != -1):
                            if map_data[point] < map_data[min_index]:
                                min_index = point
                        else:
                            min_index = point                        
                        can_add = True
                if(can_add):
                    if not used[min_index]:
                        part.append(min_index)
                        used[min_index] = 1
                    else:
                        can_add = False
                        for oneset in ret_set:
                            if min_index in oneset:
                                oneset.extend(part)
                                part = []
            if len(part) > 0:
                ret_set.append(part)
                    
        i += 1
        ret_set.sort(cmp=(lambda x,y: cmp(min(x),min(y))))
        finalret = ['a'] * len(map_data)
        for index in range(len(ret_set)):
            for index2 in ret_set[index]:
                finalret[index2] = chr(97 + index)
        stdout.write("\nCase #%d:\n" % i)
        for index in range(len(finalret)):
            if(index % W == 0 and index != 0):
                stdout.write("\n")
            stdout.write(finalret[index]);
            stdout.write(" ")
            
    f.close()
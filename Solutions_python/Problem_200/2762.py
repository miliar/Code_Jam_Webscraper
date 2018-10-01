'''
Created on Mar 19, 2016

@author: elmoatasem
'''


int2Str = lambda x:str(x) # map(int2Str,[1,2]) :  [1,2] > ['1', '2']
intList2StringList = lambda x:  map(str,x) #map(intList2StringList, [[1,3,4],[4,5,4]]) : [[1, 3, 4], [4, 5, 4]] > [['1', '3', '4'], ['4', '5', '4']]
strList2IntList = lambda x:  map(int,x)#map(strList2IntList, [['1', '3', '4'], ['4', '5', '4']]) : [['1', '3', '4'], ['4', '5', '4']] >  [[1, 3, 4], [4, 5, 4]]
strList2Str = lambda x: "".join(x) # map(strList2Str, [['1','2'],['3','4']]) : [['1','2'],['3','4']] > ['12', '34']
intList2Int = lambda x: int(strList2Str(map(int2Str,x)))# map(intList2Int, [[1,2,4,3],[6,7,8,9]]) : [[1,2,4,3],[6,7,8,9]] > [1243, 6789]
str2StrList = lambda x: list(x) # map(str2StrList, ['12','34']) : ['12','34'] > [['1', '2'], ['3', '4']] 
int2IntList = lambda x:  map(int,str2StrList(int2Str(x)))# map(Int2IntList, [123,44]):  [123,44] > [[1, 2, 3], [4, 4]]
make2DList = lambda rows,columns : [[0 for x in range(columns)] for x in range(rows)] # make2DList(r = 3,c = 5) [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# def excute_flip(string):
#     
#     for i in range(len(string)):
#         if(string[i] == '-'):
#             string[i] = '+'
#         else:    
#             string[i] = '-'
#             
#     return string[::-1]
# 
# 
# 
# def check_if_done(pattern_list):
#     done = True
#     for i in range(len(pattern_list)):
#         if(pattern_list[i] == '-'):
#             done = False
#     return done



def isTidyNumber(N):
    isTidy = True
    nList = int2IntList(N)
    for i in range(len(nList) - 1,0,-1):
        if(nList[i] == 0):
            isTidy = False
            break   
    sortedList = sorted(nList)
    if(intList2Int(sortedList) != N):
        isTidy = False

    return isTidy
    
def getLastTidyNumber(N):
    res = -1
    for j in range(N,0,-1):
        if(isTidyNumber(j)):
            res = j
            break
    return res



f_r = open('B-small-attempt0.in',"r")
n_test=int(f_r.readline().strip()) 
f_w = open("B.out", "w")
result = ""
for i in range(n_test):
    N =  int(f_r.readline().strip())
#     print pattern[0]
#     print len(pattern)
    result = getLastTidyNumber(N)
    print result
    output_str='Case #{itr}: {res}'.format(itr=(i+1),res=result)
    f_w.write(output_str+'\n')
    
f_r.close()




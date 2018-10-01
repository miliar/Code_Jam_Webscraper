import math

# def insertToArray(arr , num):
#     for i,k in enumerate(arr):
#         if k==arr[-1]:
#             arr.append(num)
#             return arr
#         elif num >=k and num<=arr[i+1]:
#             arr2 =  arr[i:]
#             arr[:i].append(num)
#             arr.extend(arr2)
#             return arr
#     return "error"

# print(insertToArray([1,2,7],3))

def solve(arr):
    mymax = max(arr)
    result = mymax
    for i in range(1,mymax):
        special = 0
        for j in arr:
            special += (j-1)//i
        result = min( result , special+i)
    return result

# print(solve([2,5,8]))

with open("B-large.in")as file:
    T = int(file.readline())
    for i in range(T):
        diners = int(file.readline())
        dishes = [int(k) for k in file.readline().strip().split(" ")]
        dishes.sort()
        # print("Case #" + str(i+1) +": " + str(dishes))
        r = solve(dishes)
        print("Case #" + str(i+1) +": " + str(r))

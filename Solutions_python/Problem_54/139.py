'''
Created on 2010-05-08

@author: lawford
'''

def find_gcf(den, arr):
#    print(str(den)+", "+str(arr))
    new_arr = [den]
    for n in arr:
        tmp = n % den
        if (tmp > 0):
            new_arr.append(tmp)
#    new_arr.append(den)
#    if len(new_arr) == 0:
#        return [den]
    return new_arr
    
def find_result(arr):
#    print(arr)
    arr = list(set(arr))
    arr.sort()
#    print(arr)
    first = arr[0]
    rest = arr[1:]
    arr = [n-first for n in rest]
#    arr = list(set(new_arr))
#    arr.sort()
    while len(arr) > 1:
#        print("in:"+str(arr))
        arr = find_gcf(arr[0], arr[1:])
        arr = list(set(arr))
        arr.sort()
#        print(arr)
    rem = arr[0]
    if first % rem == 0:
        result = 0
    else:
#        print "first="+str(first)+", step="+str(rem)
        result = rem - (first % rem)
    return (rem,result)

if __name__ == '__main__':
#    print(find_result([1,10,11]))
#    print(find_result([26,11,6]))
#    print(find_result([800000000000000000001,900000000000000000001]))
#    print(find_result([101,113,121,141,169]))
#    print(find_result([43521670, 88344644, 88344644]))
    
#    print(find_result([2,4,7]))
#    print(find_result([2,5,7]))
#    print(find_result([5,7]))
#    print(find_result([5,8]))
#    print(find_result([3375, 1344, 1343]))
#    print(find_result([636765, 175079, 577713]))
    
    f = open("/raid/downloads/firefox/B-large.in", "r")
    lines = f.readlines()
    i=1
    fout = open("/tmp/B-large.out", "w")
    for line in lines:
#        print(line)
        cols = line.split()
        if len(cols) > 1:
#            print(cols)
            intcols = [int(n) for n in cols[1:]]
            (rem,result) = find_result(intcols)
            print("Case #"+str(i)+": "+str(cols[1:])+"\t"+str([(result+n)%rem for n in intcols])+"\t"+str(rem))
            fout.write("Case #"+str(i)+": "+str(result)+"\n")
            i = i+1
    fout.close()
    f.close()

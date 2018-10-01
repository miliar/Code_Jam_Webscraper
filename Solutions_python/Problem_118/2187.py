def is_palin(val):
    if val == int(val):
        val = int(val)
    else:
        return False
    strval = str(val)
    return strval == strval[::-1]
input_line = raw_input()
N = int(input_line)
input_list = []
for i in xrange(N):
    (start,end) = raw_input().split(' ')
    num1 = int(start)
    num2 = int(end)
    input_list.append([num1,num2])
result_dict = {}
ctr = 1
for inputs in input_list:
    num1 = inputs[0]
    num2 = inputs[1]
    num=0
    for values in xrange(num1,num2+1):
        if is_palin(values) and is_palin(values**0.5):
            num+=1
    result_dict[ctr] = num
    ctr+=1
for key in result_dict:
    print "Case #"+str(key)+": "+str(result_dict[key])
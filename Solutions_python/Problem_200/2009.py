def process(num):
    l = []
    temp = num
    while temp >= 10:
        l.insert(0, temp % 10)
        if (temp % 10) < ((temp / 10) % 10):
            for i in range(len(l)):
                l[i] = 9
            temp = temp / 10 - 1
        else:
            temp = temp / 10
    if temp > 0:
        l.insert(0, temp)
        
    result = ''.join([str(x) for x in l]) 
    print(result)
    return int(result)        
        
         
          
               
def test():
    print(process(132) == 129)
    print(process(1000) == 999)
    print(process(7) == 7)
    print(process(111111111111111110) == 99999999999999999)
    print(process(1000000000000000000) == 999999999999999999)
    print(process(1) == 1)
    print(process(9) == 9)
    print(process(10) == 9)
    print(process(99) == 99)
    print(process(100) == 99)
    

test()

f = open('/sdcard/Download/B-large.in')
#f = open('/sdcard/Download/C-large-practice.in')
f_out = open('/sdcard/Download/B-large-out.txt', 'w')
#f_out = open('/sdcard/Download/C-large-practice-out.txt', 'w')
s = f.readlines()
tc_num = int(s[0])
for i in range(tc_num):
    a = int(s[i + 1])
    answer = process(a)
    print("Case #%d: %d" % (i + 1, answer))
    f_out.write("Case #%d: %d\n" % (i + 1, answer))
f.close()
f_out.close()

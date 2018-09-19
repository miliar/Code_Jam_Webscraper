f = open('small_input.txt', 'r')
o = open('ouput_file.txt', 'r+')
cases = f.readline()
cases = int(cases.strip('\n'))
ON_ARRAY = [0,1]
for x in range(1,101):
    ON_ARRAY.append(ON_ARRAY[x]*2+1)
    
for case in range(cases):
    output = 'Case #' + str(case+1) + ': '
    input = f.readline()
    N = int(input.strip('\n').split()[0])
    K = int(input.strip('\n').split()[1])
    number_on = ON_ARRAY[N]
    K -= number_on
    while K > 0:
       K -= 1
       K -= number_on
       
    if K == 0:
        output += 'ON'
    else:
        output += 'OFF'
    o.write(output + '\n')
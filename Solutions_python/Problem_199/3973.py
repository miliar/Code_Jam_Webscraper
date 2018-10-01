

#input_f = open("Q_a_test.in", "r")
#output_f = open("Q_a_test.out", "w")
input_f = open("A-small-attempt2.in", "r")
output_f = open("A-small-attempt2.out", "w")
TC = input_f.readline()
whole_data = input_f.readlines()
TIME = 0
SUCCESS = 0

def write_out(f,index,text):
    f.write('Case #%d: %d\n'%(index,text))

def reverse(str):

    if str == '-':
        return '+'
    elif str =='+':
        return '-'


def main(cake, K, index):
    global SUCCESS
    global TIME
    if len(cake)-index < K:
        if cake.find('-') == -1:
            SUCCESS = 1
        else:
            SUCCESS = 0
        return

    for i in range(index,len(cake)):
        if cake[i] == '-' and len(cake)-i >= K:
            TIME += 1
            new_cake = ''
            for j in range(len(cake)):
                if i<=j<i+K:
                    new_cake += reverse(cake[j])
                else:
                    new_cake += cake[j]
            main(new_cake,K,i+1)
            return
    main(cake,K,i)


INDEX = 0
for line in whole_data:
    INDEX += 1
    TIME = 0
    SUCCESS = 0
    pencake, K =line.split()
    main(pencake,int(K),0)
    if SUCCESS == 1:
        output_f.write('Case #%d: %d\n'%(INDEX,TIME))
    else:
        output_f.write('Case #%d: %s\n'%(INDEX,'IMPOSSIBLE'))




output_f.close()









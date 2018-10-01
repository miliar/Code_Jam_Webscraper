import sys



def output(x, y):
    return "Case #"+ str(x) + ": " + str(y)


def process_case(line):
    added = 0
    total_up = 0
    (m, ppl) = line.split(' ')
    for i in range(0, len(ppl)-1):
        total_up += int(ppl[i])
        if total_up >= (i+1):
            continue
        else:
            added+= (i+1) - total_up
            total_up+= (i+1) - total_up
        
#        if total_up >= i:
  #          total_up += int(ppl[i])
  #          if i == 0 and ppl[i] == 0
    #    else:
     #       added = (i+1)-total_up
      #      total_up+=(i+1) - total_up
    return added

def main():
    #lines = sys.stdin.readlines()
    t = input() #int(lines[0])
    result = []
    for i in range(0, int(t)):
        line = input()
        a = process_case(line)#s[i-1])
        result.append(output(i+1, a))

    with open('a.out', 'w') as f:
        for i in range(0, len(result)):
            #print(result[i])
            f.write("%s\n" % str(result[i]))
            if i % 100 == 0:
                print(str(i))

if __name__ == '__main__':
    main()
    

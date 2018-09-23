boo = 0
answers = []
n = []
with open('tidyinput.txt', 'r') as fi:
    for line in fi:
        if boo==0:
            boo = 1
        else:
            n = []
            ln = ''.join(line.split())
            for num in ln:
                n.append(int(num))
                
            #print n

            i = 1
            j = 100
            while i < len(n):
                if n[i-1] > n[i]:#If left bigger than right
                    if len(n) == 1:
                        n[0] = 9
                    elif len(n) == 2:
                        n[i-1] -= 1
                        n[i] = 9
                    else:
                        if i < 2:
                            if n[i-1] == 1:
                                n.pop(0)
                                j = 0
                            else: #n[i] > 1
                                n[i-1] -= 1
                                j = i
                            break
                        
                        elif n[i-2] < n[i-1]:#We don't have to move back
                            #Cannot be a '1'
                            j = i
                            n[i-1] -= 1
                            break

                        else:
                            while (n[i-2] == n[i-1]) and i > 1:
                                i -= 1
                            while (n[i-1] == n[i]) and i > 0:
                                i -= 1

                            if n[i] == 1: #Definitely at pos 1
                                n.pop(0)
                                j = 0
                            else: #n[i] > 1
                                n[i] -= 1
                                j = i+1
                            break
                i += 1

            while j < len(n):
                n[j] = 9
                j += 1

            n = map(str, n)
            answers.append(''.join(n))
    fi.close

val = 1
with open('tidyoutput.txt', 'a') as fi:
    for answer in answers:
        fi.write('Case #' + str(val) + ': ' + str(answer) + '\n')
        val = val+1
    fi.close

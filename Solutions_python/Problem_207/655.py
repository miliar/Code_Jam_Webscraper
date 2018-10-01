boo = 0
answers = []

with open('firstinput.txt', 'r') as fi:
    for line in fi:
        if boo==0:
            boo = 1
        else:
            [N, R, O, Y, G, B, V] = line.split()
            N = int(N)
            
            R = int(R)
            O = int(O)
            Y = int(Y)
            G = int(G)
            B = int(B)
            V = int(V)
            letters = ['R', 'O', 'Y', 'G', 'B', 'V']
            nums = [R,O,Y,G,B,V]
            #print nums

            if R > (Y+B) or Y > (R+B) or B > (R+Y):
                answers.append('IMPOSSIBLE')

            else:
                string = ''
                while (len(string) < N):
                    if len(string) > 1:
                        nums[letters.index(string[len(string) - 2])] *= -1
                    
                    i = nums.index(max(nums))
                    nums[i] -= 1
                    string += (letters[i])
                    #print string, nums

                    nums[i] *= -1

                length = len(string)
                if string[0] == string[length-1]:
                    #try swap
                    string = string[:length-2] + string[len(string)-1] + string[len(string)-2]
                    if string[0] == string[length-1]:
                        answers.append('IMPOSSIBLE')
                    answers.append(string)
                else:
                    answers.append(string)

                        
    fi.close

val = 1
with open('firstoutput.txt', 'a') as fi:
    for answer in answers:
        fi.write('Case #' + str(val) + ': ' + str(answer) + '\n')
        val = val+1
    fi.close

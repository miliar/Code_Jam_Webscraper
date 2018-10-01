with open('B-small.txt') as input_file:
    T = int(input_file.readline())
    for number_test in range(T):
        S = list(input_file.readline())
        if S[-1] == '\n':
            S = S[:-1]
        
        i = 0
        while i < len(S) - 1:
            if S[i] > S[i + 1]:
                for j in range(i + 1, len(S)):
                    S[j] = '9'
                S[i] = str(int(S[i]) - 1)
                while i > 0:
                    if S[i] < S[i - 1]:
                        S[i] = '9'
                        S[i - 1] = str(int(S[i - 1]) - 1)
                    i -= 1     
            else:
                i += 1
        print('Case #' + str(number_test+1) +': ' + str(int(''.join(S)))) 
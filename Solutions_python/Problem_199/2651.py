T = input()

def find_left_neg(s,oldleft):
    leftneg = len(s) + 1
    for j in range(oldleft,len(s)):
        if s[j]=='-':
            leftneg = j
            break
    return leftneg

def flip_next_K(s,leftneg,k):
    for i in range(k):
        s[leftneg+i] = '+' if s[leftneg+i]=='-' else '-'
    return s

for _ in range(T):
    
    s,k = raw_input().split()
    s=list(s)
    k = int(k)
    orginal_s = s
    
    leftneg = 0
    leftneg = find_left_neg(s,leftneg)
    counter = 0
    while(leftneg <= len(orginal_s)-k):  
        # forget string before this 
        # s=s[leftneg:]
        flip_next_K(s,leftneg,k)
        counter+=1
        leftneg = find_left_neg(s,leftneg)
        # print "leftneg is ", leftneg
        # print leftneg,s
        # raw_input()
    # print("finally",counter, leftneg, s)

    possible = True
    for i in s[-k-1:]:
        if i!='+':
            possible = False

    # print possible
    if possible:
        print "Case #"+str(_+1)+": "+str(counter)
    else:
        print "Case #"+str(_+1)+": ""IMPOSSIBLE"



    # remaining_all(s,'+') then true
    # remainina_all(s,'-') then +1
    #  

    # for j in range(leftneg,len(s)):
        # count+=1
        # flip next K

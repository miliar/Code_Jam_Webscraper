
# coding: utf-8

# In[1]:

def sort_tidy(N):
    M = list(map(int,str(N)))
    for k in range(0,len(M)-1):
        for i in range(0,len(M)-1):   
            if M[i]>M[i+1]:
                M[i] -= 1
                for j in range(i+1,len(M)):
                    M[j] = 9

    return int("".join(list(map(str,M))))


# In[5]:

t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
    N = int(input())
    print("Case #{}: {}".format(i, sort_tidy(N)))


f = open('C:/Users/Asis/Downloads/input6.in', 'r')
#f = open('G:/Study/Code Jam/trial.txt', 'r')
g = open('G:/Study/Code Jam/output6.txt', 'w')
no_test_cases = int(f.readline())
def change(x):
    x_str = str(x)
    changed = []
    changed.append(x)
    for i in range(1,len(x_str)):
        changee = ''
        changee = x_str[i:] + x_str[:i]
        if len(str(int(changee))) == len(changee) and int(changee) not in changed:
            changed.append(int(changee))
    return changed

for i in range(1,no_test_cases+1):
    nums_str = f.readline()
    nums = nums_str.split()
    possibilities = 0
    a = int(nums[0])
    b = int(nums[1])
    for n in range(a,b):
        m_poss = change(n)
        for m in m_poss:
            if n < m and m <= b:
                possibilities += 1
    g.write("Case #"+str(i)+": "+str(possibilities)+chr(10))
g = open('G:/Study/Code Jam/output6.txt', 'r')
f.close()
g.close()
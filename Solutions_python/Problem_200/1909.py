import sys

sys.stdout = open("./output.txt", "w")

def bubblefind(sl):
    for i in range(0, len(sl) - 1):
        if int(sl[i] <= sl[i+1]):
            pass
        else:
            sl[i] = str(int(sl[i]) - 1)
            for j in range(i + 1, len(sl)):
                sl[j] = '9'
            bubblefind(sl)

t = int(input())
for i in range(1, t + 1):
    invalid = False
    sl = list(str(raw_input()))
    bubblefind(sl)
    print('Case #{}: {}'.format(i, int("".join(sl))))

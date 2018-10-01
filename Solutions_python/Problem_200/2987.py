import fileinput

def solve(seq):
    if "1"*len(seq) > seq:
        return "9"*(len(seq)-1)
    else:
        num = "0"
        for i in range(len(seq)-1):
            num += seq[i]
            if seq[i] > seq[i + 1]:
                return (solve(str(int(num) - 1)) if num != "0" else "") + "9" * (len(seq) - i - 1)
        return seq

f = fileinput.input()
T = int(f.readline())
for case in range(1, T + 1):
    seq = f.readline()[:-1].lstrip("0")
    answer = solve(seq)
    print("Case #{0}: {1}".format(case, answer.lstrip("0") if answer != "" else "0"))
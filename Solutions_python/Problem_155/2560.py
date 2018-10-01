"""
Question 1
"""
def aud_str_to_list(aud_str):
    ans = []
    for char in aud_str:
        ans.append(int(char))
    return ans

def need_friends(line):
    s_max, aud_str = case.split()
    audience = aud_str_to_list(aud_str)
    x = 0
    for i, aud_s in enumerate(audience[1:]):
        if aud_s:
            s = sum(audience[:i+1]) + x
            if s < i+1:
                x += i+1-s
    return x

if __name__ == "__main__":

    input_file = "A-large.in"

    with open(input_file, 'r') as inp:
        lines = inp.readlines()

    result = []
    for case in lines[1:]:
        result.append(need_friends(case))

    with open(input_file.split(".")[0] + ".out", 'w') as out:
        for i, ans in enumerate(result):
            out.write("Case #{0}: {1}\n".format(i+1, ans))

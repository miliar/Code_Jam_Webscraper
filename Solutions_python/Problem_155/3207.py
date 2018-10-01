# Python 3.2
# Usage: python a.py < input.in > out.txt

cases = int(input())
for case in range(cases):
    inline = input()
    friends = 0
    audience = 0
    for bravery, c in enumerate(inline[inline.index(' ')+1:-1]):
        audience += int(c)
        while audience + friends <= bravery:
            friends += 1
    print("Case #{0}: {1}".format(case + 1, friends))

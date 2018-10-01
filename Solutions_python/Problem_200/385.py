f = open("e.in")
fout = open("e.out", "w")

input_str = f.readline()
t = int(input_str)

for case in range(1, t + 1):
    input_str = f.readline()

    arr = [ord(ch) - ord('0') for ch in input_str if ord('0') <= ord(ch) <= ord('9')]

    for x in range(len(arr) - 2, -1, -1):
        if arr[x] > arr[x + 1]:
            arr[x] -= 1
            for y in range(x + 1, len(arr)):
                arr[y] = 9

    out = 0
    for x in arr:
        out *= 10
        out += x

    fout.write("Case #%d: %d\n" % (case, out))

f.close()
fout.close()

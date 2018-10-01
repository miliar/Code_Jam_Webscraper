def run(T, inp):
    def find_duplicates(li):
        output = []
        for x in li:
            if x not in output:
                output.append(x)
        output.sort()
        return output

    n = int(inp)
    res = []
    tidy = False
    while not tidy:
        print(n)
        tot = 0
        for j in range(len(str(n))-1):
            if int(str(n)[j]) <= int(str(n)[j+1]):
                tot += 1
            else:
                break
        if tot == len(str(n))-1:
            tidy = True
        n -= 1
    res = n+1
    return res


_file = open('B-small-attempt0.in')
input_list = []
for f in _file:
    f = f.replace('\n', '')
    input_list.append(f)
_file.close()
test_cases = str(input_list[0])
input_list.pop(0)
result = []
for item in input_list:
    result.append(run(int(test_cases), item))
print(result)
_file = open('output', 'w')
for i in range(int(test_cases)+1):
        if i == int(test_cases) - 1:
            _file.write('Case #' + str(i+1) + ': ' + str(result[i]))
        else:
            _file.write('Case #' + str(i+1) + ': ' + str(result[i]) + '\n')
print('\a')

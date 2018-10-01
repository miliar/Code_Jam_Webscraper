in_file = open('pancake_flipper.in')
cases = int(in_file.readline().strip())
results = []

for case in range(cases):
    pancakes,spat_size = in_file.readline().strip().split()
    spat_size = int(spat_size)
    flips = 0
    index = 0
    while index < len(pancakes)-spat_size+1:
        if pancakes[index] == '-':
            flips+=1
            for i in range(spat_size):
                if pancakes[index+i] == '-':
                    new_cake = '+'
                else:
                    new_cake = '-'
                pancakes = pancakes[:index+i]+new_cake+pancakes[index+i+1:]
        index+=1
    if '-' not in pancakes:
        results.append("Case #{}: {}".format(case+1,flips))
    else:
        results.append("Case #{}: IMPOSSIBLE".format(case+1))
in_file.close    

out_file = open('pancake_flipper.out','w')
    
for result in results:
    print(result)
    out_file.write(result+'\n')

out_file.close
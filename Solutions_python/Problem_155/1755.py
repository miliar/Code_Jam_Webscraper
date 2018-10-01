cases = int(input())
output = []
for i in range(cases):
    maxShy,shyLevels = input().split()
    maxShy = int(maxShy)
    total = 0
    friends = 0
    
    
    for j in range(len(shyLevels)):
        if total >= j:
            total += int(shyLevels[j])
        else:
            friends += j-total;
            total += int(shyLevels[j]) + (j-total);
    
    output.append(friends)

for i in range(cases):
    print("Case #" + str(i+1) + ": " + str(output[i]))

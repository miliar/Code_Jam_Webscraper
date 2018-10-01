
def tidyNumbers(rang):

    lastTidyNum = 1

    for num in range(rang,1,-1):

        nums = [int(b) for b in str(num)]

        if sorted(nums) == nums:

            lastTidyNum = num
            break

    return lastTidyNum

t = int(input())

f = open("output.txt", "w")

for x in range(1, t + 1):
    
    num = tidyNumbers(input())

    s = "Case #" + str(x) + ": " + str(num) + "\n"
    f.write(s)
    
f.close()


    
        

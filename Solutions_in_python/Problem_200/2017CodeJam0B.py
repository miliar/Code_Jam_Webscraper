# Open the given file 
lines = open("input.txt", "r").readlines()
n = int(lines[0].strip())

# Create a function to return the last tidy number
def last_tidy(n):
    if n < 10:
        return n
    else:
        n = str(n)
        i = 0
        first = 0
        while (i < len(n) - 1) and n[i] <= n[i+1]:
            if n[i] <n[i+1]:
                first = i+1
            i = i + 1
        if i == len(n) - 1:
            return n
        answer = n[:first] + str(int(n[first]) - 1) + (len(n)-first-1)*"9"
        if answer[0] == "0":
            return answer[1:]
        else:
            return answer
        
# Create a file for the answer and line by line write last tidy number
outfile = open("answer.txt", "w")
for j in range(1,n+1):
    n = int(lines[j])
    answer = last_tidy(n)
    line = "Case #" + str(j) + ": " + str(answer) + "\n"
    outfile.write(line)
outfile.close()


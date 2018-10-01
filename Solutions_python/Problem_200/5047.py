#T = int(input())
iList = []
temp = []
L = list()

def tidy(num):
    x = list(str(num))
    x.sort()
    
    if x == list(str(num)):
        return True

    return False

def lastTidy(n):
    n = int(n)
    
    for a in range(n, 0, -1):
        if tidy(a):
            return a

# ------ METHOD ------

Type = int(input(" Input:\n\n [0: \"small\" / 1 : \"large\"]\n "))

if Type == 1:
    typeMode = "large"
else:
    typeMode = "small"

attempt = 1

filename = "B-" + typeMode + "-attempt{}".format(attempt)
    
f = open(filename + ".in", "r")     # Open input file
data = f.readlines()                # Read data
T = int(data.pop(0))                # No.of testcases
data = data[: T]                    # Limit data upto no. of tescases
f.close()                           # Explicitly closes input file

# *** display for debugging ***

print("\n T =", T)
print(" Filename =", filename)

f = open(filename + ".out", "w")    # Create NEW output file
print()
        
# ----- MAIN -----

Li = []

for a in data:
    Li.append(a.rstrip("\n"))

for a in Li:
    #num = int(input())
    L.append(lastTidy(a))

# ----- OUTPUT -----

x = 0
for a in L:
    x += 1
    print("Case #{}: {}".format(x, a))
    f.write("Case #{}: {}\n".format(x, a))

# ------ END ------

f.close()       # Explicitly closes output file to save changes

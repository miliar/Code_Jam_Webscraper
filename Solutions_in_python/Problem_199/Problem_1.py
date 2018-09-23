dic = {"+" : "-",
       "-" : "+"}

def flips(pcakes, place, Flipper):
    string = pcakes[:place-1]
    toFlip = pcakes[place-1:place+Flipper-1]
    fin = ""
    for pancake in toFlip:
        fin += dic[pancake]
    return string + fin + pcakes[place+Flipper-1:]

def simplify(pancakes,flipper,count):
    for letter in range(len(pancakes)):
        if pancakes[letter] == "-":
            if letter-1 < len(pancakes)-flipper:
                return simplify(flips(pancakes[letter:],1,flipper),flipper,count+1)
            else:
                return "IMPOSSIBLE"
    return count

TestCases = int(input(""))
number = 0
for i in range(TestCases):
    number+=1
    line = input("")
    Parts = line.split(" ")
    Pancakes = Parts[0]
    Flipper = int(Parts[1])
    result = simplify(Pancakes, Flipper, 0)
    print("CASE #" + str(number) + ": " + str(result))

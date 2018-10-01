



def flip_pancakes(pancakes, k, verbose=False):
    flipCount = 0

    max = len(pancakes) - k + 1

    if verbose:
        print(''.join(map(lambda f: '+' if f else '-', pancakes)))

    for i in range(0, max, 1):
        if not pancakes[i]:
            flipCount += 1
            for f in range(i, i + k):
                pancakes[f] = not pancakes[f]
            if verbose:
                print(''.join(map(lambda f: '+' if f else '-', pancakes)))
        
    return flipCount
        



def main():
    """ main function """
    number_of_lines = int(input())
    for n in range(1, number_of_lines + 1):
        line = input().split()
        pancakes = list(map(lambda p : p == '+', list(line[0])))
        k = int(line[1])


        flipCount = flip_pancakes(pancakes, k, False)
        print("Case #"+str(n)+": " + (str(flipCount) if all(pancakes) else "IMPOSSIBLE"))







if __name__ == "__main__":
    main()

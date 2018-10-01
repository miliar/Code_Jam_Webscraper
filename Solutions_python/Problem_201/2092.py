def stalls(N, k):
    space_distributions = [N]
    i = 0
    while k > 0:
        # maxIndex requires a list of at least len 1
        i = maxIndex(space_distributions)

        space_to_split = space_distributions[i]
        Ls = (space_to_split-1)/2
        Rs = space_to_split - 1 - Ls

        # add Ls and Rs back into the distributions
        del space_distributions[i]
        space_distributions.insert(i, Rs)
        space_distributions.insert(i, Ls)

        # don't forget to iterate
        k -= 1

    Ls = space_distributions[i]
    Rs = space_distributions[i+1]
    return (max(Ls, Rs), min(Ls, Rs))

def maxIndex(numbers):
    max_index = 0
    max_so_far = numbers[0]
    for i, num in enumerate(numbers):
        if num > max_so_far:
            max_index = i
            max_so_far = num
    return max_index

# def tests():
#     print(maxIndex([1,2,3]) == 2)
#     print(maxIndex([1,3,2]) == 1)
#     print(maxIndex([1]) == 0)
#     print(stalls(8, 2) == (2, 1))
#     print(stalls(4, 3) == (0, 0))
#     print(stalls(5, 3) == (1, 0))
#     print(stalls(4, 2) == (1, 0))
#     print(stalls(5, 2) == (1, 0))
#     print(stalls(6, 2) == (1, 1))
#     print(stalls(1000, 1000) == (0, 0))
#     print(stalls(1000, 1) == (500, 499))

# tests()

def main():
    num_problems = int(raw_input())
    for i in xrange(1, num_problems+1):
        N, k = [int(j) for j in raw_input().split(" ")]
        out = stalls(N, k)
        print "Case #{}: {} {}".format(i, out[0], out[1])

if __name__ == "__main__":
    main()

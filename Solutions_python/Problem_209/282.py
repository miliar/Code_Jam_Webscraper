import collections
import math

Pancake = collections.namedtuple('Pancake', 'r h top side')

# Template
def main():
    # Read in input
    num_test_case = int(input())

    for test_case in range(num_test_case):
        N, K = list(map(int, input().split()))
        #print(N, K)
        pancakes = []
        for n in range(N):
            radius, height = list(map(int, input().split()))
            top = math.pi * radius * radius
            side = 2 * math.pi * radius * height
            pancakes.append(Pancake(r=radius, h=height, top=top, side=side))

        #print(pancakes)
        by_total_area = sorted(pancakes, key=lambda x: x.top + x.side)

        # Greedy
        pancakes_used = [by_total_area[-1]] # Add largest
        pancakes.remove(by_total_area[-1])
        counter = 1
        while(counter < K):
            best_area = -999999999999
            best_pancake = 0
            best_position = 0
            # Add pancake which maximizes total area
            #print(pancakes)
            for new_pancake in pancakes:
                #print(new_pancake)
                position = len(pancakes_used) # Put at bottom first
                # Find position in stack
                for i in range(len(pancakes_used)):
                    if pancakes_used[i].r >= new_pancake.r:
                        position = i
                        break

                area = new_pancake.side
                # Find area contribution
                if position == len(pancakes_used):  # Pancake is at bottom
                    area += new_pancake.top - pancakes_used[-1].top

                if area >= best_area:
                    best_area = area
                    best_pancake = new_pancake
                    best_position = position

            # Insert best pancake
            pancakes_used = pancakes_used[:best_position] + [best_pancake] + pancakes_used[best_position:]
            pancakes.remove(best_pancake)
            counter += 1

        # Compute area
        area = pancakes_used[-1].top
        for pancake in pancakes_used:
            area += pancake.side

        print_solution(test_case, "{}".format(area))

def print_solution(case_number, solution_string):
    print("Case #{}: {}".format(case_number + 1, solution_string))

if __name__ == "__main__":
    main()

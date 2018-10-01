import sys
import math

def solve(instream):
    farm_price, farm_prod, target = [float(x) for x in instream.readline().strip().split(" ")]
    
    speed = 2.0
    time = 0.0

    while True:
        next_farm_time = farm_price / speed
        if target / (speed + farm_prod) + next_farm_time > target / speed:
            return time + target / speed

        time += next_farm_time
        speed += farm_prod


def run(input=sys.stdin):
    cases = int(input.readline().strip())
    for i in range(cases):
        print("Case #{}: {}".format(i + 1, solve(input)))

if __name__ == "__main__":
    run()

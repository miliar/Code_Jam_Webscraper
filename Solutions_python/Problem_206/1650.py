from typing import List, NamedTuple, Tuple, Dict, IO
from pathlib import Path


class Horse(object):
    position: float
    speed: float

    def __init__(self, position: float, speed: float):
        self.position = position
        self.speed = speed

    def position_at(self, t):
        return self.position + self.speed * t


class Case(NamedTuple):
    distance: int
    horses: List[Horse]


def read_case(f: IO) -> Case:
    horses = []
    distance, N = (int(x) for x in f.readline().split())
    for _ in range(N):
        pos, speed = (float(x) for x in f.readline().split())
        horses.append(Horse(pos, speed))


    return Case(distance, horses)


def read_input(f: IO) -> List[Case]:
    T = int(f.readline())
    return [read_case(f) for _ in range(T)]


def solve(case: Case) -> float:
    # sort them in reverse by distance
    case.horses.sort(key=lambda h: h.position, reverse=True)
    current = case.horses.pop()
    hours = float(0)
    while case.horses:
        next = case.horses.pop()
        if next.speed >= current.speed:
            continue

        d_v = current.speed - next.speed
        d_d = next.position - current.position

        time_to_horse = d_d / d_v
        time_to_dest = (case.distance - current.position) / current.speed
        min_t = min(time_to_dest, time_to_horse)
        hours += min_t

        if time_to_dest <= time_to_horse:
            break
        current = next
        current.position = current.position_at(hours)
    else:
        hours += (case.distance - current.position) / current.speed

    return case.distance / hours


def main():
    for in_path in Path('.').glob('*.in'):
        with in_path.open('r') as f:
            cases = read_input(f)

        out_path = in_path.parent / in_path.name.replace('.in', '.out')
        print(f"solving {in_path} -> {out_path}")
        with out_path.open('w') as out:
            for idx, case in enumerate(cases, start=1):
                solution = solve(case)
                print(f"Case #{idx}: {solution}", file=out)


if __name__ == '__main__':
    main()
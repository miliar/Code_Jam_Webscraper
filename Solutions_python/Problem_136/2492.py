__author__ = 'Maciej Jaworski'
import fileinput



def buy(balance, farm_cost, cps, cps_farm, target):
    time_with_farm = (target - (balance - farm_cost)) / (cps + cps_farm)
    time_no_farm = (target - balance) / cps

    if time_with_farm < time_no_farm:
        return True
    else:
        return False

def solve(farm_cost, cps_farm, target):
    current_cps = 2.0
    if farm_cost >= target:
        return target / current_cps
    else:
        balance = 0.0
        time_elapsed = 0.0
        while balance < target:
            if balance < farm_cost:
                time_elapsed += min(farm_cost, target-balance) / current_cps
                balance += min(farm_cost, target-balance)
            elif buy(balance, farm_cost, current_cps, cps_farm, target):
                balance = balance - farm_cost
                current_cps += cps_farm
            else:
                time_elapsed += min(farm_cost, target-balance) / current_cps
                balance += min(farm_cost, target-balance)

        return time_elapsed

cnt = 0
cases = 0
case = 0


for line in fileinput.input():
    if line:
        if cnt == 0:
            cases = int(line)
        else:
            case += 1
            farm_cost, cps_farm, target = [float(x) for x in line.split(' ')]
            print 'Case #{0}: {1:.7f}'.format(case, solve(farm_cost, cps_farm, target))

        cnt += 1

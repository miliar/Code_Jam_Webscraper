def time_to(cookies, production, target):
    return (target - cookies) / production

def compute(farm_cost, farm_prod, target):
    production = 2
    cookies = 0
    time = 0
    if target < farm_cost:
        return time_to(cookies, production, target)
    def go_to(new_cookies):
        nonlocal production, cookies, time, target, farm_cost, farm_prod
        action_time = time_to(cookies, production, new_cookies)
        time += action_time
        cookies += action_time * production
    def upgrade():
        nonlocal production, cookies, time, target, farm_cost, farm_prod
        cookies -= farm_cost
        production += farm_prod
    go_to(farm_cost)
    while time_to(cookies, production, target) > \
            time_to(cookies - farm_cost, production + farm_prod, target):
        upgrade()
        go_to(farm_cost)
    go_to(target)
    return time

T = int(input())
for i in range(1, T + 1):
    args = [float(w) for w in input().split()]
    print("Case #{}: {}".format(i, compute(*args)))

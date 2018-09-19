def invite(case, m, string):
    people_needed = 0
    tiers = [i for i in range(len(string))]
    people = [int(string[i]) for i in range(len(string))]
    current_tier = 0
    while current_tier <= max(tiers):
        if sum(people[:current_tier + 1]) >= (current_tier + 1):
            current_tier += 1
        else:
            people[current_tier] += 1
            people_needed += 1
    return "Case #%i: %i\n" % (case, people_needed)

with open('A-large.in', 'r') as f:
    lines = f.readlines()

i = 1
result = []

for l in lines:
    if len(l.split(' ')) == 2:
        args = sum([[i], [i.strip() for i in l.split(' ')]], [])
        result.append(invite(*args))
        i += 1

with open('A-large.out', 'w') as f:
    f.writelines(result)

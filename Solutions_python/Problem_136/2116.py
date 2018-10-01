#
# Aldo Mendoza
# Google Code Jam
#   Qualification Round 2014
# aldus.91@gmail.com
#

#
# Process a single case and returns a string with the result
#
def process_case():
    initial_rate = 2.0

    line = raw_input().split(' ')
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])

    result = X / initial_rate
    max_farms = X / C

    time_taken = [0]
    rate = [initial_rate]

    for farms in range(1, int(max_farms) + 1):
        time_taken.append(time_taken[farms - 1] + (C / rate[farms - 1]))
        rate.append(initial_rate + (farms * F))
        total_time = time_taken[farms] + (X / rate[farms])

        if total_time < result:
            result = total_time

    return result


#
# Entry point
#
T = int(raw_input())

for case in range(1, T + 1):
    print "Case #%d: %.7f" % (case, process_case())

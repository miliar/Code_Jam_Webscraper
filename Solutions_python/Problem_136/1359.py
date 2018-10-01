def get_cookie_data(lines):
    count = int(lines[0])
    lines = lines[1:]
    result = []
    for line in lines:
        c, f, x = [float(item) for item in line.split(" ")]
        result.extend([{"c": c, "f": f, "x": x}])
    return result


def get_sec_count(c, f, x):
    rate = 2
    total_time = 0
    initial_wait = x/rate
    if c/rate >= initial_wait:
        return initial_wait
    farming = 0
    while True:
        farming += c/rate
        rate += f
        just_wait = x/rate
        if farming + just_wait >= total_time and total_time != 0:
            return total_time
        if farming + just_wait > initial_wait:
            return initial_wait
        total_time = farming + just_wait


if __name__ == '__main__':
    with open("B-large.in", "rb") as f:
        data = f.read()

    lines = data.split("\n")
    datasets = get_cookie_data(lines)
    results = []
    for i, case in enumerate(datasets):
        t = get_sec_count(case["c"], case["f"], case["x"])
        results.extend(["Case #{0}: {1:.7f}".format(i+1, t)])

    with open("pb_results.in", "wb") as f:
        f.write("\n".join(results))

import sys


def parset(text):
    lines = [i.strip() for i in text.split("\n") if i.strip()]
    num = int(lines.pop(0))
    test_cases = []
    for line in lines:
        both = []
        orange = []
        blue = []
        split = line.split()
        split.pop(0)
        while split:
            color = split.pop(0)
            button = int(split.pop(0))
            both.append((color, button))
            if color == "O":
                orange.append(button)
            else:
                blue.append(button)
        test_cases.append({"both":both, "orange": orange, "blue": blue})
    return test_cases

def get_time(case):
    total_time = 0
    orange = 1
    blue = 1
    last_pushed_index = 0
    
    while case["both"]:
        next_orange = case["orange"][0] if case["orange"] else orange
        next_blue = case["blue"][0] if case["blue"] else blue
        od = abs(orange-next_orange)
        bd = abs(blue-next_blue)
        t = min(od, bd)
        total_time += t
    
        if od > bd:
            orange = orange-next_orange if next_orange<orange else next_orange
            blue = next_blue
        else:
            blue = blue-next_blue if next_blue<blue else next_blue
            orange = next_orange
    
        next_button = case["both"][0]
        if next_button[0] == "O":
            if next_button[1] == orange:
                case["both"].pop(0)
                total_time += 1
        else:
            if next_button[1] == blue:
                case["both"].pop(0)
                total_time += 1
    return total_time
    
    
def get_time2(case):
    total_time = 0
    orange = 1
    blue = 1
    last_pushed_index = 0
    
    while case["both"]:
        next_orange = case["orange"][0] if case["orange"] else None
        next_blue = case["blue"][0] if case["blue"] else None
        next_button = case["both"][0]
        
        # Check if button needs pressing
        if next_button[0] == "O":
            if next_button[1] == orange:
                case["both"].pop(0)
                case["orange"].pop(0)
                total_time += 1
                if next_blue and next_blue != blue:
                    blue += 1 if next_blue > blue else -1
                continue
        else:
            if next_button[1] == blue:
                case["both"].pop(0)
                case["blue"].pop(0)
                total_time += 1
                if next_orange and next_orange != orange:
                    orange += 1 if next_orange > orange else -1
                continue
        
        # Move otherwise
        if next_orange and next_orange != orange:
            orange += 1 if next_orange > orange else -1
        if next_blue and next_blue != blue:
            blue += 1 if next_blue > blue else -1
        total_time += 1
    return total_time
    
def get_times(parsed):
    for ind, case in enumerate(parsed):
        print "Case #%s: %s" % (ind+1, get_time2(case))


if __name__ == '__main__':
   get_times(parset(open(sys.argv[1]).read()))
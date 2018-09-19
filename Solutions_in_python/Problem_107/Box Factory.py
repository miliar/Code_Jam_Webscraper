import sys

def search(toys, boxes):
    #print(toys, boxes)
    if len(toys) == 0 or len(boxes) == 0: return 0
    t = toys[:]
    b = boxes[:]
    v = 0
    if t[0][1] == b[0][1]:
        # Same type
        mn = min(t[0][0], b[0][0])
        #print(mn)
        if t[0][0] == mn:
            if b[0][0] == mn:
                v = max(search(t[1:], b[1:]) + mn, v)
            else:
                v = max(search(t[1:], [[b[0][0]-mn, b[0][1]]] + b[1:]) + mn, v)
        elif b[0][0] == mn:
            v = max(search([[t[0][0]-mn, t[0][1]]] + t[1:], b[1:]) + mn, v)
        return v
    v = max(search(t, b[1:]), v)
    v = max(search(t[1:], b), v)
    return v


def box_factory(args, toys, boxes):
    toys = toys.split(' ')
    boxes = boxes.split(' ')
    toys = [[int(toys[i]), int(toys[i+1])] for i in range(0, len(toys), 2)]
    boxes = [[int(boxes[i]), int(boxes[i+1])] for i in range(0, len(boxes), 2)]
    #print(toys, boxes)
    return str(search(toys, boxes))

def main(filename):
    Input = open(filename, 'r').read().split('\n')
    Output = ""
    for i in range(1, int(Input[0]) + 1):
        args = Input[3*i-2]
        toys = Input[3*i-1]
        boxes = Input[3*i]
        #print(toys, boxes)
        result = box_factory(args, toys, boxes)
        Output += "Case #" + str(i) + ": " + result + "\n"
    open(filename[:-3] + ".out", 'w').write(Output)

if __name__ == "__main__": main(sys.argv[1])

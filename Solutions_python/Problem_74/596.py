import sys

class Bot(object):
    def __init__(self):
        self.buttons = []
        self.index = 0
        self.loc = 1
    def add_button(self, button):
        self.buttons.append(button)
    def move(self, limit=None):
        if not self.isDone():
            old_loc = self.loc
            dest = self.buttons[self.index]
            if limit:
                distance = min(limit, abs(dest - self.loc))
                if dest > self.loc:
                    self.loc += distance
                else:
                    self.loc -= distance
            else:
                self.loc = dest
                return abs(self.loc - old_loc)
    def push(self):
        self.index += 1
        return 1
    def isDone(self):
        return self.index == len(self.buttons)
        
def go(filename):
    with open(filename) as f:
        with open("out.txt", "w") as output:
            for case in range(1, int(f.readline()) + 1):
                tokens = f.readline().split()[1:]
                seq = zip(*[iter(tokens)] * 2)
                orange = Bot()
                blue = Bot()
                prio = []
                for v in seq:
                    bot = blue if v[0] == "B" else orange
                    prio.append(bot)
                    bot.add_button(int(v[1]))
                time = 0
                for prio_bot in prio:
                    t = prio_bot.move()
                    t += prio_bot.push()
                    (blue if prio_bot is orange else orange).move(t)
                    time += t
                output.write("Case #%d: %d\n" % (case, time))
                    

                
                      

def main():
    if len(sys.argv) < 1:
        print "Usage: %s <filename>" % os.path.basename(sys.argv[0])
    else:
        go(sys.argv[1])

if __name__ == "__main__":
    main()

INPUT = {
     'data' : (('int', 'int'), 'constant')
}

TEST = ('''\
4
1 0
1 1
4 0
4 47
''','''\
Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON
''')

def main(data):
    N, K = data
    
    x = 2**N
    
    return "ON" if 1 == (x- K % x) else "OFF"
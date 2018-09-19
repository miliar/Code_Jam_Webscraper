# Finde ein bestimmtes "Wort" in einem Gitter.
# Ein "pivot"-Element wird uebernommen. Wenn das Wort gefunden wird,
# wird die Spalte zurueckgegeben, in der das "pivot"-Element liegt.
# zB. wird bei "[H, A, L, L, O], 1" die Spalte mit dem A zurueckgegeben."

def find_combo(board, pattern, pivot):
    x = find_combo_horizontal(board, pattern, pivot)
    if x >= 0:
        return x

    # Bei vertikalen Mustern liegen alle Elemente in derselben Spalte; kein pivot.
    x = find_combo_vertical(board, pattern)
    if x >= 0:
        return x
    
    # Bend:
    #  0
    #   0
    #    0
    x = find_combo_bend(board, pattern, pivot)
    if x >= 0:
        return x

    # Sinister:
    #     0
    #    0
    #   0
    x = find_combo_sinister(board, pattern, pivot)
    if x >= 0:
        return x

    return -1

# Finde horizontale Muster
def find_combo_horizontal(board, pattern, pivot):
    width = len(board[0])
    for row in board:
        for start in range(0, width + 1 - len(pattern)):
            match = 1
            matchrev = 1
            for x in range(0, len(pattern)):
                match = match and row[start + x] == pattern[x]
                matchrev = matchrev and row[start + x] == pattern[len(pattern) - 1 - x]
                if not (match or matchrev):
                    break
            if match:
                return start + pivot
            elif matchrev:
                return start + len(pattern) - 1 - pivot

    return -1

# Vertikale Muster
def find_combo_vertical(board, pattern):
    height = len(board)
    width = len(board[0])
    for col in range(0, width):
        for start in range(0, height + 1 - len(pattern)):
            match = 1
            matchrev = 1
            for y in range(0, len(pattern)):
                match = match and board[start + y][col] == pattern[y]
                matchrev = matchrev and board[start + y][col] == pattern[len(pattern) - 1 - y]
                if not (match or matchrev):
                    break
            if match or matchrev:
                return col
    return -1

# Links oben nach rechts unten
def find_combo_bend(board, pattern, pivot):
    height = len(board)
    width = len(board[0])
    # X entlang des linken Randes, dann entlang des oberen Randes.
    startleft = [0] * height + range(1, width)
    # Y entlang des linken Randes, dann entlang des oberen Randes
    starttop = range(0, height) + [0] * (width - 1)
    for left, top in zip(startleft, starttop):
        dist_to_edge = min(width - left, height - top)
        for offset in range(0, dist_to_edge - len(pattern) + 1):
            match = 1
            matchrev = 1
            for z in range(0, len(pattern)):
                match = match and board[top + offset + z][left + offset + z] == pattern[z]
                matchrev = matchrev and board[top + offset + z][left + offset + z] == pattern[len(pattern) - 1 - z]
                if not (match or matchrev):
                    break
            if match:
                return left + offset + pivot
            elif matchrev:
                return left + offset + len(pattern) - 1 - pivot

    return -1

# Rechts oben nach links unten        
def find_combo_sinister(board, pattern, pivot):
    height = len(board)
    width = len(board[0])
    # X entlang des linken Randes, dann entlang des unteren Randes.
    startleft = [0] * height + range(1, width)
    # Y entlang des linken Randes, dann entlang des unteren Randes.
    starttop = range(0, height) + [height - 1] * (width - 1)
    for left, top in zip(startleft, starttop):
        dist_to_edge = min(width - left, top + 1)
        for offset in range(0, dist_to_edge - len(pattern) + 1):
            match = 1
            matchrev = 1
            for z in range(0, len(pattern)):
                match = match and board[top - offset - z][left + offset + z] == pattern[z]
                matchrev = matchrev and board[top - offset - z][left + offset + z] == pattern[len(pattern) - 1 - z]
                if not (match or matchrev):
                    break
            if match:
                return left + offset + pivot
            elif matchrev:
                return left + offset + len(pattern) - 1 - pivot

    return -1
